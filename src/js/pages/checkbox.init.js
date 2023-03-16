// function selectAll(){
//     var items=document.getElementsByName('datePosted');
//     for(var i=0; i<items.length; i++){
//         if(items[i].type=='checkbox')
//             items[i].checked=true;
//     }
// }

// function UnSelectAll(){
//     var items=document.getElementsByName('datePosted');
//     for(var i=0; i<items.length; i++){
//         if(items[i].type=='checkbox')
//             items[i].checked=false;
//     }
// }


var checkAll = document.getElementById("checkAll");
        if (checkAll) {
            checkAll.onclick = function() {
                var checkboxes = document.querySelectorAll('.form-check-all input[type="checkbox"]');
                for(var i=0; i < checkboxes.length; i++) {
                    checkboxes[i].checked = this.checked;
                }
            }
        }