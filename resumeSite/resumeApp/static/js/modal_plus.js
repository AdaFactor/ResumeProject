$(document).ready(() => {
    var optEducation = $("#id_education option").length;
    var optReference = $("#id_reference option").length;
    var optLanguage = $("#id_language option").length;
    var optSkill = $("#id_skill option").length;
    var optExperience = $("#id_experience option").length;

    $("#education-save").click(() => {
        optEducation++;
        var newAcademy = $("#id_academy_name").val();
        $("#id_education").append('<option value=' + optEducation + '>' + newAcademy + '</option>');
    });

    $("#reference-save").click(() => {
        optReference++;
        var newAdvisor = $("#id_advisor_name").val();
        $("#id_reference").append('<option value=' + optReference + '>' + newAdvisor + '</option>');                
    });
    
    $("#language-save").click(() => {
        optLanguage++;
        var newLanguage = $("#id_name_language").val();
        $("#id_language").append('<option value=' + optLanguage + '>' + newLanguage + '</option>');
    });

    $("#skill-save").click(() => {
        optSkill++;
        var newSkill = $("#id_name_skill").val();
        $("#id_skill").append('<option value=' + optSkill + '>' + newSkill + '</option>');
    });

    $("#experience-save").click(() => {
        optExperience++;
        var newExperience = $("#id_company_name").val();
        $("#id_experience").append('<option value=' + optExperience + '>' + newExperience + '</option>');
    });
});