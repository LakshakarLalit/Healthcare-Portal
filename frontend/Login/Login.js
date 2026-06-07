document.addEventListener("DOMContentLoaded", () => {
    const patientTabBtn = document.getElementById("btn-patient-tab");
    const adminTabBtn = document.getElementById("btn-admin-tab");
    const patientForm = document.getElementById("patient-login-form");
    const adminForm = document.getElementById("admin-login-form");
    
    const regFields = document.getElementById("registration-fields");
    const ageInput = document.getElementById("p-age");
    const genderSelect = document.getElementById("p-gender");
    const patientSubmitBtn = document.getElementById("patient-submit-btn");
    
    const patientMsg = document.getElementById("patient-message");
    const adminMsg = document.getElementById("admin-message");

    // Clear messages helper
    function showMessage(element, text, type = "error") {
        element.textContent = text;
        element.style.display = "block";
        if (type === "error") {
            element.style.backgroundColor = "#fee2e2";
            element.style.borderColor = "#fca5a5";
            element.style.color = "#b91c1c";
        } else if (type === "info") {
            element.style.backgroundColor = "#eff6ff";
            element.style.borderColor = "#bfdbfe";
            element.style.color = "#1d4ed8";
        } else if (type === "success") {
            element.style.backgroundColor = "#ecfeff";
            element.style.borderColor = "#bae6fd";
            element.style.color = "#0891b2";
        }
    }

    function clearMessage(element) {
        element.style.display = "none";
        element.textContent = "";
    }

    // Tab toggling logic
    patientTabBtn.addEventListener("click", () => {
        patientTabBtn.classList.add("active");
        adminTabBtn.classList.remove("active");
        patientForm.classList.add("active");
        adminForm.classList.remove("active");
        clearMessage(patientMsg);
        clearMessage(adminMsg);
    });

    adminTabBtn.addEventListener("click", () => {
        adminTabBtn.classList.add("active");
        patientTabBtn.classList.remove("active");
        adminForm.classList.add("active");
        patientForm.classList.remove("active");
        clearMessage(patientMsg);
        clearMessage(adminMsg);
    });

    // Patient login & signup submission
    patientForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        clearMessage(patientMsg);

        const name = document.getElementById("p-name").value.trim();
        const phone = document.getElementById("p-phone").value.trim();

        if (phone.length !== 10 || isNaN(phone)) {
            showMessage(patientMsg, "Mobile number must be a 10-digit number.");
            return;
        }

        try {
            // Fetch all patients from backend to verify credentials
            const res = await fetch("http://127.0.0.1:8000/patient/getall/");
            if (!res.ok) throw new Error("Could not connect to medical server database.");
            
            const result = await res.json();
            const patients = result.data || [];
            
            // Find patient with matching name (case-insensitive) and phone number
            const matchedPatient = patients.find(p => 
                p.name.toLowerCase() === name.toLowerCase() && 
                String(p.phone) === phone
            );

            if (matchedPatient) {
                // Patient exists, log them in!
                sessionStorage.setItem("userRole", "patient");
                sessionStorage.setItem("userName", matchedPatient.name);
                sessionStorage.setItem("patientId", matchedPatient.id);
                sessionStorage.setItem("patientPhone", matchedPatient.phone);
                
                showMessage(patientMsg, "Redirecting...", "success");
                setTimeout(() => {
                    window.location.href = "../Home/Home.html";
                }, 800);
            } else {
                // Check if registration fields are already showing
                const isRegShowing = regFields.classList.contains("reg-fields-visible");
                
                if (!isRegShowing) {
                    // Reveal registration inputs
                    regFields.classList.remove("reg-fields-hidden");
                    regFields.classList.add("reg-fields-visible");
                    
                    ageInput.required = true;
                    genderSelect.required = true;
                    
                    patientSubmitBtn.textContent = "Register & Sign In";
                    showMessage(patientMsg, "Complete one-time registration fields below.", "info");
                } else {
                    // If showing, proceed with registration POST
                    const age = ageInput.value;
                    const gender = genderSelect.value;

                    if (!age || !gender) {
                        showMessage(patientMsg, "Please fill out Age and Gender fields.");
                        return;
                    }

                    // Register new patient profile
                    const regRes = await fetch("http://127.0.0.1:8000/patient/patient/", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({
                            name: name,
                            phone: phone,
                            age: parseInt(age),
                            gender: gender,
                            disease: "New Patient Registration",
                            city: "Mumbai",
                            state: "Maharashtra",
                            avatar: gender === "Female" 
                                ? "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=256&h=256&q=80"
                                : "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=256&h=256&q=80"
                        })
                    });

                    if (!regRes.ok) throw new Error("Database registration rejected.");
                    const regResult = await regRes.json();

                    if (regResult.message === "Success") {
                        const newPatient = regResult.data;
                        
                        sessionStorage.setItem("userRole", "patient");
                        sessionStorage.setItem("userName", newPatient.name);
                        sessionStorage.setItem("patientId", newPatient.id);
                        sessionStorage.setItem("patientPhone", newPatient.phone);
                        
                        showMessage(patientMsg, "Account registered! Redirecting...", "success");
                        setTimeout(() => {
                            window.location.href = "../Home/Home.html";
                        }, 800);
                    } else {
                        showMessage(patientMsg, "Failed to register profile. " + JSON.stringify(regResult.data));
                    }
                }
            }
        } catch (error) {
            console.error("Auth error:", error);
            showMessage(patientMsg, "Error checking registration state: " + error.message);
        }
    });

    // Admin login submission
    adminForm.addEventListener("submit", (e) => {
        e.preventDefault();
        clearMessage(adminMsg);

        const username = document.getElementById("a-username").value.trim();
        const accessPin = document.getElementById("a-password").value.trim();

        if (username === "admin" && accessPin === "0000000000") {
            sessionStorage.setItem("userRole", "admin");
            sessionStorage.setItem("userName", "Administrator");
            
            showMessage(adminMsg, "Authenticated! Redirecting to panel...", "success");
            setTimeout(() => {
                window.location.href = "../Home/Home.html";
            }, 800);
        } else {
            showMessage(adminMsg, "Invalid administrator username or access PIN.");
        }
    });
});
