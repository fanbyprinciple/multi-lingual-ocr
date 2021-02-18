// 1 6mm?” 2 msmﬁnmmﬁqﬁmm,°ﬁﬁ1ﬁmmsmﬁ$w 3 Wuﬁﬁﬁmaﬁaﬁemmﬁmw|m A Wﬁammmm|ﬁmﬁﬁm 5 mmfiﬂwaﬁmﬁﬁwwmﬁﬁm a Wgoﬁmwwaﬁmawmﬁmm 7 mammsaawwaﬁau—QWWW s m| 

$( document ).ready(function() {
    console.log( "ready player one!" );

    const worker = Tesseract.create();

    const defaultImage = "static/bengali_text.png"
    //const defaultImage = 'https://tesseract.projectnaptha.com/img/eng_bw.png';
    // const defaultImage = 'https://i.redd.it/8h66m4nnyo331.jpg';
    // const defaultImage = 'https://i.imgur.com/fun6Hrl.png';


    const ocr = document.querySelector('#ocr');
    const input = ocr.querySelector('#ocr__input');
    const img = ocr.querySelector('#ocr__img');
    const output = ocr.querySelector('#ocr__output');
    const form = ocr.querySelector('#ocr__form');


    input.value = defaultImage;
    img.src = defaultImage;


    function myError(err, message) {	
        console.warn(`MyError: ${message || ''}`);
        console.error(err);
    }

    async function recognizeImage(image) {
        console.log('recognize START');
        worker.terminate();
        
        output.textContent = 'Waiting to start.';
        output.classList.remove('error');
        output.classList.add('processing');
        
        return worker.recognize(image)
            .progress(progress => {
                // console.log('progress', progress);
                output.innerHTML = `Processing...<br>Status: ${progress.status}<br>${Math.round(progress.progress * 100)}%`;
            }).then(result => {
                // console.log('result', result);

                output.classList.remove('processing');
                output.textContent = result.text;
            }).catch(err => {
                myError(err, 'caught error');
                output.classList.add('error');
                output.textContent = 'Error processing image.';
            }).finally(() => {
                console.log('recognize END');		
                worker.terminate();
            });
    }

    form.onsubmit = async e => {
        console.log('submit START');
        e.preventDefault();
        
        const imageUrl = input.value;
        img.src = imageUrl;
        
        await recognizeImage(imageUrl);
        
        console.log('submit END');
    }

});







