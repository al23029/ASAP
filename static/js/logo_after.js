window.addEventListener('scroll', function() {
    var logoWhite = document.getElementById('logo-white');
    var logoNavy = document.getElementById('logo-navy');
    
    if (window.scrollY > 1) {
        // スクロール位置が1pxを超えたらロゴを切り替える
        logoWhite.style.display = 'none';
        logoNavy.style.display = 'block';
    } else {
        // スクロール位置が1px未満に戻ったら元のロゴに戻す
        logoWhite.style.display = 'block';
        logoNavy.style.display = 'none';
    }
});
