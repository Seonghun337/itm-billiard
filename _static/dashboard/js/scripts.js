function init(){
    $( "#player_3" ).hide();
    $( "#player_4" ).hide();

    $('#rank_pagination').twbsPagination({
        visiblePages: 7,
        onPageClick: function (event, page){
            $('').text('Page ' + page);
        }
    })
}
init();
function createPlayerInputs(event){
    let n = event.target.value;
    if (n==2){
        $("#player_3").hide();
        $("#player_4").hide();
    }
    else if(n==3){
        $("#player_3").show();
        $("#player_4").hide();
    }else{
        $("#player_3").show();
        $("#player_4").show();
    }
    
}

function showScore(target_id){
    
    document.getElementById(target_id + "_value").innerText = document.getElementById(target_id).value;
    
}



function incrementScore(event){
    let id = event.target.value
    let t = document.getElementById(id)

    t.value = parseInt(t.value) + 10;
    showScore(id);
}

function decrementScore(event){
    let id = event.target.value
    let t = document.getElementById(id)

    t.value = parseInt(t.value) - 10;
    showScore(id);
}


//======= temporary pagination part
var n_game_per_page = 5;
function game_pagination_init(){
    var n_page = Math.ceil(n_games / n_game_per_page);
    var game_page_html = "";
    // game_page_html += "<nav aria-label='...'>";
    game_page_html += "<ul class='pagination pagination-sm'>";
    for(var i=0;i<n_page;i++){
        game_page_html += "<li class='page-item'>";
        game_page_html += "<button id='game_page_btn_"+
        i+ "' class='page-link' value=" +
        i+ " onclick='game_pagination(event)'>";
        game_page_html += String(i+1);
        game_page_html += "</button>";
        game_page_html += "</li>";
    }
    game_page_html += "</ul>";
    // game_page_html += "</nav>";
    console.log(game_page_html);
    // document.getElementById("game-pagination").innerHTML = game_page_html;
    tmp = document.createElement('nav');
    tmp.setAttribute("aria-label","...");
    tmp.setAttribute("class","float-right");
    tmp.innerHTML = game_page_html;
    document.getElementById("game-pagination").appendChild(tmp);

    document.getElementById("game_page_btn_0").click()
}

game_pagination_init();


function game_pagination(event){
    let page_num_now = event.target.value;
    for(var i=0;i<n_games;i++){
        if(i >= page_num_now * n_game_per_page && i < (page_num_now+1) * n_game_per_page){
            // document.getElementById("game_tr_"+i).style.display = 'inline';
            $("#game_tr_"+i).show();
        }else{
            $("#game_tr_"+i).hide();
        }
    }

}

var n_rank_per_page = 5;
function rank_pagination_init(){
    var n_page = Math.ceil(n_rank / n_rank_per_page);
    var rank_page_html = "";
    rank_page_html += "<ul class='pagination pagination-sm'>";
    for(var i=0;i<n_page;i++){
        rank_page_html += "<li class='page-item'>";
        rank_page_html += "<button id='rank_page_btn_"+
        i+ "' class='page-link' value=" +
        i+ " onclick='rank_pagination(event)'>";
        rank_page_html += String(i+1);
        rank_page_html += "</button>";
        rank_page_html += "</li>";
    }
    rank_page_html += "</ul>";
    tmp = document.createElement('nav');
    tmp.setAttribute("aria-label","...");
    // tmp.setAttribute("class","float-right");
    tmp.innerHTML = rank_page_html;
    document.getElementById("rank-pagination").appendChild(tmp);

    document.getElementById("rank_page_btn_0").click()
}

rank_pagination_init();


function rank_pagination(event){
    let r_page_num_now = event.target.value;
    for(var i=0;i<n_rank;i++){
        if(i >= r_page_num_now * n_rank_per_page && i < (r_page_num_now+1) * n_game_per_page){
            $("#rank_tr_"+i).show();
        }else{
            $("#rank_tr_"+i).hide();
        }
    }

}

//=======