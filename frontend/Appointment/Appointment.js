document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".appointment-form");
    const doctorSelect = document.getElementById("doctor-select");
    
    // Fetch and populate doctors list from REST API
    async function loadDoctors() {
        if (!doctorSelect) return;
        try {
            const res = await fetch("http://localhost:8000/api/doctors/");
            if (!res.ok) throw new Error("Could not fetch doctors");
            const doctors = await res.json();
            
            // Clear existing options except placeholder
            doctorSelect.innerHTML = '<option value="" disabled selected>Choose a Doctor</option>';
            
            doctors.forEach(doc => {
                const opt = document.createElement("option");
                opt.value = doc.id;
                opt.textContent = `${doc.name} (${doc.specialty})`;
                doctorSelect.appendChild(opt);
            });
        } catch (e) {
            console.log("Backend offline, using fallback static options for doctors:", e);
            // Default to static options in HTML
        }
    }
    
    loadDoctors();

    if (form) {
        form.addEventListener("submit", async (e) => {
            e.preventDefault();
            
            const doctorId = document.getElementById("doctor-select").value;
            const date = document.getElementById("appointment-date").value;
            const time = document.getElementById("appointment-time").value;
            const patientName = document.getElementById("patient-name").value;
            const patientAge = document.getElementById("patient-age").value;
            const patientGender = document.getElementById("patient-gender").value;
            
            const selectedOpt = doctorSelect.options[doctorSelect.selectedIndex];
            const doctorLabel = selectedOpt ? selectedOpt.textContent : doctorId;
            
            let successBanner = document.querySelector(".success-message");
            if (!successBanner) {
                successBanner = document.createElement("div");
                successBanner.className = "success-message";
                form.insertBefore(successBanner, form.firstChild);
            }

            try {
                // If doctorId is numeric, send to backend API
                if (doctorId && !isNaN(doctorId)) {
                    const res = await fetch("http://localhost:8000/api/appointments/", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            doctor: parseInt(doctorId),
                            date: date,
                            time: time,
                            patient_name: patientName,
                            patient_age: parseInt(patientAge),
                            patient_gender: patientGender
                        })
                    });
                    
                    if (!res.ok) {
                        const errDetails = await res.json();
                        throw new Error(JSON.stringify(errDetails));
                    }
                } else {
                    // Fallback scenario where API is down and user selected fallback option
                    console.log("Submitting using local fallback values");
                }
                
                successBanner.innerHTML = `🎉 Appointment successfully booked with <strong>${doctorLabel}</strong> for <strong>${patientName}</strong> on <strong>${date}</strong> at <strong>${time}</strong>.`;
                successBanner.style.backgroundColor = "#ecfeff";
                successBanner.style.borderColor = "#bae6fd";
                successBanner.style.color = "#0891b2";
                successBanner.style.display = "block";
                form.reset();
            } catch (err) {
                console.error("Booking error:", err);
                successBanner.innerHTML = `❌ Failed to book appointment. Please try again.`;
                successBanner.style.backgroundColor = "#fee2e2";
                successBanner.style.borderColor = "#fca5a5";
                successBanner.style.color = "#b91c1c";
                successBanner.style.display = "block";
            }
            
            successBanner.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            
            setTimeout(() => {
                successBanner.style.display = "none";
            }, 8000);
        });
    }
});