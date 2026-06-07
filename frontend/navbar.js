document.addEventListener("DOMContentLoaded", () => {
    const role = sessionStorage.getItem("userRole");
    const name = sessionStorage.getItem("userName");
    
    // Page pathname routing check
    const currentPath = window.location.pathname.toLowerCase();
    const isLoginPage = currentPath.includes("login.html");
    
    // 1. Authentication Gate
    if (!role && !isLoginPage) {
        window.location.href = "../Login/Login.html";
        return;
    }
    
    // 2. Authorization Gate (Admin Only for Patient Records Database)
    if (currentPath.includes("patients.html") && role !== "admin") {
        alert("🔒 Access Denied: Patient admission records are restricted to administrators only.");
        window.location.href = "../Home/Home.html";
        return;
    }
    
    // 3. Dynamic Navbar Rendering
    const nav = document.querySelector("nav");
    if (nav) {
        // Clear hardcoded placeholder html
        nav.innerHTML = "";
        
        // Brand logo
        const logo = document.createElement("h2");
        logo.textContent = "The Care Hospital";
        logo.style.cursor = "pointer";
        logo.addEventListener("click", () => {
            if (role) {
                window.location.href = "../Home/Home.html";
            } else {
                window.location.href = "../Login/Login.html";
            }
        });
        nav.appendChild(logo);
        
        // Check if user is logged in before rendering links list
        if (role) {
            const ul = document.createElement("ul");
            
            // Home link
            const liHome = document.createElement("li");
            const aHome = document.createElement("a");
            aHome.href = "../Home/Home.html";
            aHome.textContent = "Home";
            if (currentPath.includes("home.html")) aHome.style.borderBottom = "2px solid white";
            liHome.appendChild(aHome);
            ul.appendChild(liHome);
            
            // Doctors link
            const liDoc = document.createElement("li");
            const aDoc = document.createElement("a");
            aDoc.href = "../Doctor/Doctor.html";
            aDoc.textContent = "Doctors";
            if (currentPath.includes("doctor.html")) aDoc.style.borderBottom = "2px solid white";
            liDoc.appendChild(aDoc);
            ul.appendChild(liDoc);
            
            // Role-based links
            if (role === "admin") {
                const liPat = document.createElement("li");
                const aPat = document.createElement("a");
                aPat.href = "../Patients/Patients.html";
                aPat.textContent = "Patients Database";
                if (currentPath.includes("patients.html")) aPat.style.borderBottom = "2px solid white";
                liPat.appendChild(aPat);
                ul.appendChild(liPat);
            } else {
                const liApp = document.createElement("li");
                const aApp = document.createElement("a");
                aApp.href = "../Appointment/Appointment.html";
                aApp.textContent = "Book Appointment";
                if (currentPath.includes("appointment.html")) aApp.style.borderBottom = "2px solid white";
                liApp.appendChild(aApp);
                ul.appendChild(liApp);
            }
            
            // Logout link
            const liLogout = document.createElement("li");
            const aLogout = document.createElement("a");
            aLogout.href = "#";
            aLogout.innerHTML = `Logout <span style="font-size: 0.8rem; font-weight: normal; opacity: 0.9;">(${name})</span>`;
            aLogout.addEventListener("click", (e) => {
                e.preventDefault();
                sessionStorage.clear();
                window.location.href = "../Login/Login.html";
            });
            liLogout.appendChild(aLogout);
            ul.appendChild(liLogout);
            
            nav.appendChild(ul);
        }
    }
});
