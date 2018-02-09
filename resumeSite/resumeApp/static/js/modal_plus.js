$(document).ready(() => {
    var optEducation = $("#id_education option").length;
    var optReference = $("#id_reference option").length;
    var optLanguage = $("#id_language option").length;
    var optSkill = $("#id_skill option").length;
    var optExperience = $("#id_experience option").length;
    
    $("#educate").validate({
        rules: {
            academy_name: "required",
            level_education: "required",
            major: "required",
            branch: "required",
            course: "required",
            time_period: "required",
        },
        messages: {
            academy_name: "Please specify academy name",
            level_education: "Please specify level",
            major: "Please specify major",
            branch: "Please specify branch",
            course: "Please specify course",
            time_period: "Please specify time period",
        },
        submitHandler: (form) => {
            optEducation++;
            var newAcademy = $("#id_academy_name").val();
            $(".modal").modal("hide");
            $("#id_education").append('<option value=' + optEducation + '>' + newAcademy + '</option>');
        }
    })
    $("#education-save").click(() => {
        $("#educate").valid();
    });

    $("#reference").validate({
        rules: {
            advisor_name: "required",
            position: "required",
            affiliation: "required",
            phone_no: "required",
            email: "required",
        },
        messages: {
            advisor_name: "Please specify advisor name",
            position: "Please specify position",
            affiliation: "Please specify affiliation",
            phone_no: "Please specify phone",
            email: "Please specify email",
        },
        submitHandler: (form) => {
            optReference++;
            var newAdvisor = $("#id_advisor_name").val();
            $(".modal").modal("hide");            
            $("#id_reference").append('<option value=' + optReference + '>' + newAdvisor + '</option>');
        }
    });
    $("#reference-save").click(() => {
        $("#reference").valid();
    });

    $("#language").validate({
        rules: {
            name_language: "required",
            level_language: "required",
        },
        messages: {
            name_language: "Please specify language",
            level_language: "Please specify level",
        },
        submitHandler: (form) => {
            optLanguage++;
            var newLanguage = $("#id_name_language").val();
            $(".modal").modal("hide");                    
            $("#id_language").append('<option value=' + optLanguage + '>' + newLanguage + '</option>');
            
        }
    });
    $("#language-save").click(() => {
        $("#language").valid();
    });

    $("#skill").validate({
        rules: {
            name_skill: "required",
            level_skill: "required",
        },
        messages: {
            name_skill: "Please specify skill",
            level_skill: "Please specify level",
        },
        submitHandler: (form) => {
            optSkill++;
            var newSkill = $("#id_name_skill").val();
            $(".modal").modal("hide");                    
            $("#id_skill").append('<option value=' + optSkill + '>' + newSkill + '</option>');
            
        }
    });
    $("#skill-save").click(() => {
        $("#skill").valid();
    });

    $("#experience").validate({
        rules: {
            company_name: "required",
            position: "required",
            role: "required",
            time_period: "required",
        },
        messages: {
            company_name: "Please specify company name",
            position: "Please specify position",
            role: "Please specify role",
            time_period: "Please specify time period",
        },
        submitHandler: (form) => {
            optExperience++;
            var newExperience = $("#id_company_name").val();
            $(".modal").modal("hide");                                
            $("#id_experience").append('<option value=' + optExperience + '>' + newExperience + '</option>');
        }
    });
    $("#experience-save").click(() => {
        $("#experience").valid();
    });

    // $("#education-save").click(() => {
    //     optEducation++;
    //     var newAcademy = $("#id_academy_name").val();
    //     $("#id_education").append('<option value=' + optEducation + '>' + newAcademy + '</option>');
    //  });

    // $("#reference-save").click(() => {
    //     optReference++;
    //     var newAdvisor = $("#id_advisor_name").val();
    //     $("#id_reference").append('<option value=' + optReference + '>' + newAdvisor + '</option>');                
    // });
    
    // $("#language-save").click(() => {
    //     optLanguage++;
    //     var newLanguage = $("#id_name_language").val();
    //     $("#id_language").append('<option value=' + optLanguage + '>' + newLanguage + '</option>');
    // });

    // $("#skill-save").click(() => {
    //     optSkill++;
    //     var newSkill = $("#id_name_skill").val();
    //     $("#id_skill").append('<option value=' + optSkill + '>' + newSkill + '</option>');
    // });

    // $("#experience-save").click(() => {
    //     optExperience++;
    //     var newExperience = $("#id_company_name").val();
    //     $("#id_experience").append('<option value=' + optExperience + '>' + newExperience + '</option>');
    // });

});