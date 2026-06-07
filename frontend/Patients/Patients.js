let tableBody = document.getElementById("patientTableBody")

async function getData()
{
    try {
        let res = await fetch("http://localhost:8000/api/appointments/");
        if (!res.ok) throw new Error("Network response was not ok");
        let data = await res.json();
        display(data);
    } catch (e) {
        console.log("Failed to fetch appointments from backend, using dummy data fallback:", e);
        // Fallback local dummy data to ensure visual rendering when served statically
        let dummyPatients = [
            { id: "PT-1024", name: "Ramesh Sharma", age: 45, gender: "Male", disease: "Coronary Artery Disease", doctor: "Dr. Firoz Sharma", admissionDate: "2026-05-15", status: "Admitted" },
            { id: "PT-2055", name: "Aarav Patel", age: 6, gender: "Male", disease: "Acute Bronchitis", doctor: "Dr. Ananya Iyer", admissionDate: "2026-06-01", status: "Discharged" },
            { id: "PT-3091", name: "Meera Nair", age: 34, gender: "Female", disease: "Chronic Migraine", doctor: "Dr. Vikram Roy", admissionDate: "2026-05-28", status: "Observation" },
            { id: "PT-4022", name: "Kriti Sen", age: 28, gender: "Female", disease: "Atopic Dermatitis", doctor: "Dr. Sneha Kapoor", admissionDate: "2026-06-02", status: "Observation" },
            { id: "PT-5018", name: "Vijay Malhotra", age: 58, gender: "Male", disease: "Osteoarthritis", doctor: "Dr. Rahul Verma", admissionDate: "2026-05-10", status: "Admitted" },
            { id: "PT-6077", name: "Suman Rao", age: 49, gender: "Female", disease: "Pneumonia", doctor: "Dr. Priya Patel", admissionDate: "2026-05-24", status: "Critical" }
        ];
        display(dummyPatients);
    }
}

function display(allPatients)
{
    tableBody.innerHTML = "";
    for(let i of allPatients)
    {
        // Custom styling mapping for gender badges
        let genderClass = 'badge-other';
        if (i.gender.toLowerCase() === 'male') {
            genderClass = 'badge-male';
        } else if (i.gender.toLowerCase() === 'female') {
            genderClass = 'badge-female';
        }

        // Custom styling mapping for status badges
        let statusClass = 'badge-discharged';
        if (i.status.toLowerCase() === 'admitted') {
            statusClass = 'badge-admitted';
        } else if (i.status.toLowerCase() === 'observation' || i.status.toLowerCase() === 'under observation') {
            statusClass = 'badge-observation';
        } else if (i.status.toLowerCase() === 'critical') {
            statusClass = 'badge-critical';
        }

        tableBody.innerHTML += `
        <tr>
            <td class="patient-id">${i.id}</td>
            <td class="patient-name">${i.name}</td>
            <td>${i.age}</td>
            <td><span class="badge ${genderClass}">${i.gender}</span></td>
            <td>${i.disease}</td>
            <td>${i.doctor}</td>
            <td>${i.admissionDate}</td>
            <td><span class="badge ${statusClass}">${i.status}</span></td>
        </tr>
        `;
    }
}

getData();