function copyFunction() {
    var copyText = document.getElementById("{{image.id}}");
    button = Button(root, text = "copy link", command=self.select())
    button.pack()
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */
    document.execCommand("copy");
    alert("Link Copied: " + copyText.value);

}