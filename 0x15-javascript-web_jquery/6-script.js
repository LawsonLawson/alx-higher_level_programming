/* global $ */

/**
 * This script updates the text of the <header> element to "New Header!!!"
 * when the <div> element with the id "update_header" is clicked.
 *
 * The script uses the jQuery selector `$` to select the <div> element with the id "update_header".
 * It attaches a click event handler that changes the text of the <header> element when
 * the <div> is clicked.
 *
 * Note:
 * - This script assumes that jQuery is loaded and available in the HTML document.
 * - It is recommended to ensure that this script is executed after the DOM is fully loaded.
 * - This script is intended to be semistandard compliant with the flag --global $.
 */

/* Use jQuery to attach a click event handler to the <div> with id "update_header" */
$('div#update_header').click(function () {
  /* Change the text of the <header> element to "New Header!!!" */
  $('header').text('New Header!!!');
});
