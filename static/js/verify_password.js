
// function to build the JSON and send to the POST API over http endpoint
function verifyPassword(password, imageURL){
    // calling POST API
    var request = {};
    request["password"] = password;

    $.ajax({
    url: "http://localhost:5000/retrieve/" + imageURL + "/verify_password",
    type: "POST",
    data: JSON.stringify(request),
    contentType: "application/json",
    success: function(result){
    console.log("success")
    console.log(result)
    window.location.href = result["url"]
    },
    error: function(error){
    console.log(`Error ${error}`)
    }
    })
}


