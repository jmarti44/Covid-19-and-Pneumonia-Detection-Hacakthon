var doctorClicked = false;
var patientClicked = false;

function doctorClick(){
    if(patientClicked == true)
        patientClicked = false;
    doctorClicked = true;
    console.log("Doctor clicked " + doctorClicked);
    console.log("patient clicked " + patientClicked);
}

function patientClick(){
    if (doctorClicked == true){
        doctorClicked = false;
    }
    console.log("patient clicked " + patientClicked);
    console.log("Doctor clicked " + doctorClicked);
}

function onSubmit(){
    if(patientClicked == true){
        location.href = "/patient.html"
    }
    else if(doctorClicked == true){
        window.location.href = "/doctor.html"
    }
}