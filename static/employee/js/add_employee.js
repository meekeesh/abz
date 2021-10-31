const apiURL  = 'http://127.0.0.1:8000/employee-set/new-employee'

function getCookie(name) {
	let cookieValue =null

	if (document.cookie && document.cookie != '') {
		let cookies = document.cookie.split(';')

		for (let el in cookies) {
			let cookie = cookies[el].trim()

			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
				break
			}
		}
	}
	return cookieValue
}

function sendData() {
	const contextData = {
		name            : document.getElementById("name").value,
		position        : document.getElementById("position").value,
		salary          : document.getElementById("salary").value,
		parent          : document.getElementById("chief").value,
		employment_date : document.getElementById("employment_date").value,
	}

	const formData = new FormData()
	for (let el in contextData) {
		formData.append(el, contextData[el])
	}

	if (document.querySelector('input[type="file"]').files.length > 0) {
		formData.append('photo', document.querySelector('input[type="file"]').files[0])
	}

	fetch(apiURL, {
		method : "POST",
		headers : {
			'X-CSRFToken': getCookie('csrftoken')
		},
		body: formData
	})
}


let name = ''

function getRequestUrl() {
	const requestParam = `?name=${name}`
	const apiURL = 'http://127.0.0.1:8000/chief-set/'
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
				document.getElementsByTagName("datalist")[0].innerHTML += 
				`
					<option value="${el.id}">${el.name} - ${el.position}</option>
				`
				})
			})
}

function getName(value) {
	name = value
	chiefQueryset()
}
