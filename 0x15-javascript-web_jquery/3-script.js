/* global $ */

/**
 * This script uses the jQuery API to add a "red" class to the <header> element,
 * which changes its color to red, when the <div> element with the id "red_header" is clicked.
 *
 * The script uses the jQuery selector `$` to select the <div> element with the id "red_header".
 * It attaches a click event handler that adds the "red" class to the <header> element
 * when the <div> is clicked.
 *
 * Note:
 * - This script assumes that jQuery is loaded and available in the HTML document.
 * - It is recommended to ensure that this script is executed after the DOM is fully loaded.
 * - The "red" class should be defined in the CSS to set the desired red color for the <header> element.
 * - This script is intended to be semistandard compliant with the flag --global $.
 */

/* Use jQuery to attach a click event handler to the <div> with id "red_header" */
$('div#red_header').click(function () {
  /* When the <div> is clicked, add the "red" class to the <header> element */
  $('header').addClass('red');
});
