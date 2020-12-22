function registration()
{
    const json = {
        "first_name": document.getElementById("first_name").value,
        "last_name": document.getElementById("last_name").value,
        "email": document.getElementById("email").value,
        "password": document.getElementById("password").value
    };

    $.post({
        url: "/auth/register/",
        data: JSON.stringify(json),
        dataType: "json",
        contentType: "application/json",
        success: function (data)
        {
            console.log("Success");
        },
        error: function (data)
        {
            console.log("Error");
        }
    });
}