function showForm(element) {
    console.log(element.getAttribute("formId"));
    document.getElementById(element.getAttribute("formId")).style.display = "block";
}

function hideForm(element) {
    console.log(element.getAttribute("formId"));
    document.getElementById(element.getAttribute("formId")).style.display = "none";
}