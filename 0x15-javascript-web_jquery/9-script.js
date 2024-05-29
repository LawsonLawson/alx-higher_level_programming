/* global $ */

/**
 * This script fetches data from an API endpoint and updates the text content of
 * the <div> element with the id "hello" based on the response data.
 *
 * The script uses the jQuery method $.get() to send an AJAX GET request to the
 * specified URL ('https://fourtonfish.com/hellosalut/?lang=fr').
 * When the request is successful, it retrieves the 'hello' message from the response data
 * and sets the text content of the <div> element with id "hello" to the retrieved message.
 *
 * Note:
 * - This script assumes that jQuery is loaded and available in the HTML document.
 * - It is recommended to ensure that this script is executed after the DOM is fully loaded.
 * - This script is intended to be semistandard compliant with the flag --global $.
 */

/* Fetch data from the specified API endpoint using jQuery $.get() method */
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus) {
  /* Update the text content of the <div> element with id "hello" to the retrieved message */
  $('DIV#hello').text(data.hello);
});
