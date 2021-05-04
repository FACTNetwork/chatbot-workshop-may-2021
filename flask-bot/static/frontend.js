// When the page has loaded, run a function to attach a submit
// handler to the user input form.
window.onload = function () {
    document.getElementById('ask').onsubmit = async function (e) {
        // Stop the normal form submit process as we are going to 
        // process it here instead.
        e.preventDefault();

        alert('The Submit button was pressed.');

    };
}