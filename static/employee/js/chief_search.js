const apiURL = 'http://127.0.0.1:8000/chief-set/'
let name = ''

function getRequestUrl() {
	const requestParam = `?name=${name}`
	const requestURL = apiURL + requestParam

	return requestURL
}

function chiefQueryset() {
	const url = getRequestUrl()
	document.getElementsByTagName("datalist")[0].innerHTML = ''

	fetch(url)
		.then(response => response.json())
		.then(data => {
			data.map(el => {
				console.log(el.name)
				document.getElementsByTagName("datalist")[0].innerHTML += 
				`
					<option value="${el.id}">${el.name} - ${el.position}</option>
				`
				})
			})
}

function getName() {
	name = document.querySelector('.chief').children[0].value.trim()
	chiefQueryset()
}
