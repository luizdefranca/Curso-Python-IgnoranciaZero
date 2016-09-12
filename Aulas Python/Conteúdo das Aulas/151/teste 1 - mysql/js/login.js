/**
 * Created by pedro on 23/03/2016.
 */

$(document).ready(function () {

    // Seleciona as principais divs e forms
    var $formLogin = $("#login-form");
    var $formLost = $('#lost-form');
    var $formRegister = $('#register-form');
    var $divForms = $('#div-forms');
    var $modalAnimateTime = 300;
    var $msgAnimateTime = 150;
    var $msgShowTime = 2000;

    // Adiciona a troca de divs aos botoes
    $("#login_register_btn").on("click", function (e) {e.preventDefault(); modalAnimate($formLogin, $formRegister);});
    $('#register_login_btn').on("click", function (e) {e.preventDefault(); modalAnimate($formRegister, $formLogin); });
    $('#login_lost_btn').on("click", function (e) {e.preventDefault(); modalAnimate($formLogin, $formLost); });
    $('#lost_login_btn').on("click", function (e) {e.preventDefault(); modalAnimate($formLost, $formLogin); });
    $('#lost_register_btn').on("click", function (e) {e.preventDefault(); modalAnimate($formLost, $formRegister); });
    $('#register_lost_btn').on("click", function (e) {e.preventDefault(); modalAnimate($formRegister, $formLost); });

    function modalAnimate ($oldForm, $newForm) {
        var $oldH = $oldForm.height();
        var $newH = $newForm.height();
        $divForms.css("height",$oldH);
        $oldForm.fadeToggle($modalAnimateTime, function(){
            $divForms.animate({height: $newH}, $modalAnimateTime, function(){
                $newForm.fadeToggle($modalAnimateTime);
            });
        });
    }
});