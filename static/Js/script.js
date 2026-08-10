document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("riskForm");

    if (!form) {
        return;
    }


    const predictButton =
        document.getElementById("predictButton");


    const requiredFields =
        form.querySelectorAll("[required]");


    function validateField(field) {

        if (!field.value.trim()) {

            field.classList.add("invalid");

            return false;
        }

        field.classList.remove("invalid");

        return true;
    }


    requiredFields.forEach(function (field) {

        field.addEventListener("change", function () {

            validateField(field);

        });


        field.addEventListener("input", function () {

            validateField(field);

        });

    });


    form.addEventListener("submit", function (event) {

        let isValid = true;


        requiredFields.forEach(function (field) {

            if (!validateField(field)) {

                isValid = false;

            }

        });


        const bmiField =
            document.getElementById("BMI");


        if (bmiField.value) {

            const bmi =
                parseFloat(bmiField.value);


            if (bmi < 10 || bmi > 80) {

                bmiField.classList.add("invalid");

                isValid = false;

                alert(
                    "Please enter a BMI value between 10 and 80."
                );
            }
        }


        if (!isValid) {

            event.preventDefault();

            const firstInvalid =
                form.querySelector(".invalid");

            if (firstInvalid) {

                firstInvalid.focus();

            }

            return;
        }


        if (predictButton) {

            predictButton.disabled = true;

            predictButton.innerHTML =
                "<span>Analyzing Risk...</span>";

            predictButton.style.opacity = "0.75";

            predictButton.style.cursor = "wait";
        }

    });

});