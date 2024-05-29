/**
 * This script updates the text color of the HTML <header> element to red (#FF0000).
 *
 * The script uses the `document.querySelector` method to select the <header> element
 * and then changes its CSS color property to red.
 *
 * Note:
 * - This script assumes that there is a <header> element present in the HTML document.
 * - It does not use jQuery and directly manipulates the DOM using vanilla JavaScript.
 * - Ensure this script is executed after the DOM is fully loaded to avoid any null references.
 */

/* Select the <header> element and update its text color to red */
document.querySelector('header').style.color = '#FF0000';
