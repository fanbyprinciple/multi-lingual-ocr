// 1 6mm?” 2 msmﬁnmmﬁqﬁmm,°ﬁﬁ1ﬁmmsmﬁ$w 3 Wuﬁﬁﬁmaﬁaﬁemmﬁmw|m A Wﬁammmm|ﬁmﬁﬁm 5 mmfiﬂwaﬁmﬁﬁwwmﬁﬁm a Wgoﬁmwwaﬁmawmﬁmm 7 mammsaawwaﬁau—QWWW s m| 

$( document ).ready(function() {
    console.log( "ready player one!" );

    // const worker = Tesseract.create();

    const defaultImage = "static/aa.jpg"
    //const defaultImage = 'https://tesseract.projectnaptha.com/img/eng_bw.png';
    // const defaultImage = 'https://i.redd.it/8h66m4nnyo331.jpg';
    // const defaultImage = 'https://i.imgur.com/fun6Hrl.png';


    const ocr = document.querySelector('#ocr');
    const input = ocr.querySelector('#ocr__input');
    const img = ocr.querySelector('#o__img');
    const output = ocr.querySelector('#ocr__output');
    const form = ocr.querySelector('#ocr__form');
    const result = ocr.querySelector('.o__textarea')


    input.value = defaultImage;
    img.src = defaultImage;
    imageUrl = input.value;

    function myError(err, message) {	
        console.warn(`MyError: ${message || ''}`);
        console.error(err);
    }

    function recognizeImage(imageUrl) {
        console.log('recognize START');
        
        // worker.terminate();
        
        output.textContent = 'Put the url for image and press start.';
        output.classList.remove('error');
        output.classList.add('processing');

        $.post("recog",{'image':imageUrl}, function(data){
       
        }).progress(progress => {
            // console.log('progress', progress);
            output.innerHTML = `Processing...<br>Status: ${progress.status}<br>${Math.round(progress.progress * 100)}%`;
            console.log('inside progress')
        }).done(function(data){
            // console.log('result', result);
            console.log(data['data'])
            output.classList.remove('processing');
            output.textContent = 'Translation successful. Look into console for logs.';
            // output.css("background-color", "Lime")
            result.textContent = data['data']

        }).catch(err => {
            console.log('inside catch')
            myError(err, 'caught error');
            output.classList.add('error');
            // output.css("background-color", "Maroon")
            output.textContent = 'Error processing image. Check python console for logs.';
        })
    }

    form.onsubmit = e => {
        console.log('submit START ');
        e.preventDefault();
        
        const imageUrl = input.value;
        img.src = imageUrl;
        
        console.log(imageUrl)

        recognizeImage(imageUrl);
        
        console.log('submit END');
    }

});







