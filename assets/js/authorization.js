function authorization()
{
    const json = {
        "email": document.getElementById("email").value,
        "password": document.getElementById("password").value
    };

    $.post({
        url: "/auth/login/",
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
