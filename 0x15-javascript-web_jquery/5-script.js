/* global $ */

/**
 * This script adds a new <li> element with the text "Item" to the <ul> element
 * with the class "my_list" when the <div> element with the id "add_item" is clicked.
 *
 * The script uses the jQuery selector `$` to select the <div> element with the id "add_item".
 * It attaches a click event handler that appends a new <li> element to the <ul> element
 * with the class "my_list" when the <div> is clicked.
 *
 * Note:
 * - This script assumes that jQuery is loaded and available in the HTML document.
 * - It is recommended to ensure that this script is executed after the DOM is fully loaded.
 * - This script is intended to be semistandard compliant with the flag --global $.
 */

/* Use jQuery to attach a click event handler to the <div> with id "add_item" */
$('div#add_item').click(function () {
  /* Define the new <li> element to be added */
  const element = '<li>Item</li>';
  /* Append the new <li> element to the <ul> with class "my_list" */
  $('ul.my_list').append(element);
});
