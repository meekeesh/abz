const apiURL = 'http://127.0.0.1:8000/chief-set/'

let name = ''

let dropDownList = []


function getRequestUrl() {
	const requestParam = `?name=${name}`
	const requestURL = apiURL + requestParam

	return requestURL
}

function chiefQueryset() {
	const url = getRequestUrl()
	fetch(url)
		.then(response => response.json())
		.then(data => {
			data.map(el => {
			dropDownList.push(el.name)
			})
		})
}

function getName() {
	name = document.querySelector('.chief').children[0].value.replace(/\s/g, '%20')
	chiefQueryset()
}
