$('#table-attendance').DataTable( {
    paging: true,
    // "lengthChange": false
    // "lengthMenu": [ 10, 25, 50, 75, 100 ]
} );
$('#table-home-work').DataTable( {
    paging: true,
} );
$('#table-task').DataTable( {
    paging: true,
} );
$('#table-requests').DataTable( {
    paging: true,
} );

$('#table-ideas').DataTable( {
    paging: true,
} );

$('#table-recent-request').DataTable( {
    paging: false,
    searching: false,
    info: false,
} );

$(document).ready(function() {
    $('#table-presence').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            'excel'
        ]
    } );
} );

$('#table-users').DataTable( {
    paging: true,
} );

$('#table-report').DataTable( {
    paging: true,
} );
