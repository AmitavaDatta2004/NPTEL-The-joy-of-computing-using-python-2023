function copyCode(codeId) {
    /* Get the text inside the pre element */
    var code = document.getElementById(codeId).textContent;
  
    /* Select the text field */
    var textField = document.createElement("textarea");
    textField.value = code;
  
    /* Select the body element */
    var body = document.getElementsByTagName("body")[0];
  
    /* Append the textarea element to the body to enable selection */
    body.appendChild(textField);
  
    /* Select the entire content of the text area */
    textField.select();
  
    /* Copy the selected text */
    document.execCommand("copy");
  
    /* Remove the textarea element from the body */
    body.removeChild(textField);
  
    /* Alert the user that the code has been copied */
    alert("The code has been copied to your clipboard.");
  }
  