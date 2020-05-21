
function loadHTML(element, src) {
	var xhr = new XMLHttpRequest()
	xhr.open('GET', src, true)
	xhr.onload = function() {element.innerHTML = this.responseText}
	xhr.send()
}

function loadAllHTML(src) {
	var elements, i, att = 'include-html'
	elements = document.querySelectorAll('['+att+']')
	for (i=0; i<elements.length; i++) {
		loadHTML(elements[i], elements[i].getAttribute(att))
		elements[i].removeAttribute(att)
	}
}


function toggleGallery() {
	gallery = document.querySelector('.gallery')
	gallery.classList.toggle('active')
	// button = gallery.querySelector('button')
	// alert(button)
	document.body.append('hi')
}
