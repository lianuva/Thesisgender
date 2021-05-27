document.addEventListener("DOMContentLoaded", function(debug=true) {
let os1 = document.getElementById("os1").value;

document.getElementById("os1").value = "unknown";

function getOS() {
    var userAgent = window.navigator.userAgent,
        platform = window.navigator.platform,
        macosPlatforms = ["Macintosh", "MacIntel", "MacPPC", "Mac68K"],
        windowsPlatforms = ["Win32", "Win64", "Windows", "WinCE"],
        iosPlatforms = ["iPhone", "iPad", "iPod"];

    if (macosPlatforms.indexOf(platform) !== -1) {
    os1 = 'Mac OS';
    } else if (iosPlatforms.indexOf(platform) !== -1) {
    os1 = 'iOS';
    } else if (windowsPlatforms.indexOf(platform) !== -1) {
    os1 = 'Windows';
    } else if (/Android/.test(userAgent)) {
    os1 = 'Android';
    } else if (!os && /Linux/.test(platform)) {
    os1 = 'Linux';
    } 
    return os1;
}

// os1 = getOS();
document.getElementById("os1").value = getOS();
});

