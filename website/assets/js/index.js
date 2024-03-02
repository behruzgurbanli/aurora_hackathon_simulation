$(document).ready(function() {
    // Get the value of data-id attribute
    var dataId = $(".health-info").attr("data-id");

    // Check if dataId is equal to 1
    if (dataId == 1) {
        // Enable goodinfo and goodicon classes
        $(".goodinfo").show();
        $(".goodicon").show();
        // Hide badinfo and badicon classes
        $(".badinfo").hide();
        $(".badicon").hide();
    } else if (dataId == 0) {
        // Enable badinfo and badicon classes
        $(".badinfo").show();
        $(".badicon").show();
        // Hide goodinfo and goodicon classes
        $(".goodinfo").hide();
        $(".goodicon").hide();
    }
});