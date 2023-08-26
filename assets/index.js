
window.onload = function() {
    var moreBtn = document.getElementById("more");
    moreBtn.onclick = function load_more() {
        var ana1 = document.getElementById("ana2")
        if(moreBtn.innerHTML === "more...") {
            var new_inner = `<h3>Analysis 2</h3>
                <p style="font-size: small;">
                    firstly, established IPs contribute significantly to generating high income in the movie industry. 
                    Secondly, action elements are prevalent in high-income movies. Thirdly, famous directors appeal more to the market and gain higher income.
                </p>
                <h3>Analysis 3</h3>
                <p style="font-size: small;">
                    firstly, established IPs contribute significantly to generating high income in the movie industry. 
                    Secondly, action elements are prevalent in high-income movies. Thirdly, famous directors appeal more to the market and gain higher income.
                </p>
                `
            ana1.innerHTML = new_inner
            moreBtn.innerHTML = "show less"
        } else {
            var new_inner = `<h3>Analysis 2</h3>
                <p style="font-size: small;">
                    firstly, established IPs contribute significantly to generating high income in the movie industry. 
                    Secondly, action elements...</p>
                `
            ana1.innerHTML = new_inner
            moreBtn.innerHTML = "more..."
        }
    }
}