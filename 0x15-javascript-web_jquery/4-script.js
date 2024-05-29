/* global $ */

/**
 * This script toggles the class of the <header> element between "red" and no class
 * when the <div> element with the id "toggle_header" is clicked.
 *
 * The script uses the jQuery selector `$` to select the <div> element with the id "toggle_header".
 * It attaches a click event handler that toggles the "red" class on the <header> element
 * when the <div> is clicked.
 *
 * Note:
 * - This script assumes that jQuery is loaded and available in the HTML document.
 * - It is recommended to ensure that this script is executed after the DOM is fully loaded.
 * - The "red" class should be defined in the CSS to set the desired red color for the <header> element.
 * - This script is intended to be semistandard compliant with the flag --global $.
 */

/* Use jQuery to attach a click event handler to the <div> with id "toggle_header" */
$('div#toggle_header').click(function () {
  /* When the <div> is clicked, toggle the "red" class on the <header> element */
  $('header').toggleClass('red');
});
