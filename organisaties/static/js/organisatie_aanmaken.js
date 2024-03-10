function genereerApiKey() {
    var alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    var apiKey = '';
    for (var i = 0; i < 32; i++) {
        apiKey += alphabet.charAt(Math.floor(Math.random() * alphabet.length));
    }
    document.getElementById('api_key').value = apiKey;
}
