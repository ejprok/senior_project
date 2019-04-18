
$(function() {
  // whenever we hover over a menu item that has a submenu
  $('#menuwrapper ul').children('li').on('mouseover', function() {
    var $menuItem = $(this),
        $submenuWrapper = $('> ul', $menuItem);
    
    console.log($menuItem, $submenuWrapper);
    
    // grab the menu item's position relative to its positioned parent
    var menuItemPos = $menuItem.position();
    
    // place the submenu in the correct position relevant to the menu item
    $submenuWrapper.css({
      top: menuItemPos.top,
      left: menuItemPos.left + Math.round($menuItem.outerWidth())
    });
  });
});