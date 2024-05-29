/* global $ */

/**
 * This script uses the jQuery API to change the text color of the HTML <header> element to red (#FF0000).
 *
 * The script uses the jQuery selector `$` to select the <header> element
 * and then applies the `css` method to change its `color` property to red.
 *
 * Note:
 * - This script assumes that jQuery is loaded and available in the HTML document.
 * - It is recommended to ensure that this script is executed after the DOM is fully loaded.
 * - This script is intended to be semistandard compliant with the flag --global $.
 */

/* Use jQuery to select the <header> element and update its text color to red */
$('header').css('color', '#FF0000');
