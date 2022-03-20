window.onload = () => {
    const video = document.querySelector("#camera");
    const canvas = document.querySelector("#picture");
    const se = document.querySelector('#se');

    /** カメラ設定 */
    const constraints = {
        audio: false,
        video: {
            width: 300,
            height: 200,
            facingMode: { exact: "environment" }  // リアカメラを利用する場合
        }
    };

    /**
     * カメラを<video>と同期
     */
    navigator.mediaDevices.getUserMedia(constraints)
        .then((stream) => {
            video.srcObject = stream;
            video.onloadedmetadata = (e) => {
                video.play();
            };
        })
        .catch((err) => {
            console.log(err.name + ": " + err.message);
        });

    /**
     * シャッターボタン
     */
    document.querySelector("#shutter").addEventListener("click", () => {
        const ctx = canvas.getContext("2d");

        // canvasに画像を貼り付ける
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        const photoData = canvas.toDataURL();
        data = {
            'name': document.getElementById('name').value,
            'kind': document.getElementById('kind').value,
            'note': document.getElementById('note').value,
            'price': parseInt(document.getElementById('price').value),
            'photo_data': photoData
        }

        let body = JSON.stringify(data);
        let headers = { 'Accept': 'application/json', 'Content-Type': 'application/json' };
        let method = "POST";

        fetch("/api/v1/items", { method, headers, body }).then(() => {
            alert('post')
        })
    });
}