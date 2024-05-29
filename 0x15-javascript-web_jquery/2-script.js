/* global $ */

/**
 * This script uses the jQuery API to change the text color of the HTML <header> element to red (#FF0000)
 * when the <div> element with the id "red_header" is clicked.
 *
 * The script uses the jQuery selector `$` to select the <div> element with the id "red_header".
 * It attaches a click event handler that changes the color of the <header> element to red
 * when the <div> is clicked.
 *
 * Note:
 * - This script assumes that jQuery is loaded and available in the HTML document.
 * - It is recommended to ensure that this script is executed after the DOM is fully loaded.
 * - This script is intended to be semistandard compliant with the flag --global $.
 */

/* Use jQuery to attach a click event handler to the <div> with id "red_header" */
$('div#red_header').click(function () {
  /* When the <div> is clicked, change the color of the <header> element to red */
  $('header').css('color', '#FF0000');
});
