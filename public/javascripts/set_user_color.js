$(function () {
    console.log("AAAAAAAAAAAAAA");
    $("#group-footer > ul").each(function (index, element) {
        console.log(index);
        if (index == 0) continue;
        if (index > 10) return;

        var colors = ["#c44857", "#a1d85b", "#9f4bc4", "#5f8645", "#532e62",
            "#c9883a", "#928dc6", "#76c8ba", "#504338", "#ceb09f"];

        $(element).find(".shape").css("background-color", colors[index - 1]);
    });
});