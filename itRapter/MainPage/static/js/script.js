function loadData() {
  return new Promise((resolve, reject) => {
    setTimeout(resolve, 2000);
  })
}

loadData()
  .then(() => {
    let preloaderEl = document.getElementById('preloader');
    preloaderEl.classList.add('hidden');
    preloaderEl.classList.remove('visible');
  });



$(document).ready(function() {
   // Assuming that your element that would be wrapped comes as second td (column).
   // If not, adjst the nth-child(2).
   $('#result_list tbody tr td:nth-child(2)').each(function(e) {
        $(this).expander({
            slicePoint:       50,  // default is 100
            expandSpeed: 0,
            expandEffect: 'show',
            collapseSpeed: 0,
            collapseEffect: 'hide',
            expandPrefix:     ' ', // default is '... '
            expandText:       '[...]', // default is 'read more'
            userCollapseText: '[^]'  // default is 'read less'
        });
   });
});