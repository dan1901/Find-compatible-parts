document.addEventListener('DOMContentLoaded', function() {
    var selectElems = document.querySelectorAll('select');
    var selectInstances = M.FormSelect.init(selectElems);

    var modalElems = document.querySelectorAll('.modal');
    var modalInstances = M.Modal.init(modalElems);

    var tooltipElems = document.querySelectorAll('.tooltipped');
    var tooltipInstances = M.Tooltip.init(tooltipElems);
});