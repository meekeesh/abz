const apiInfoURL  = 'http://127.0.0.1:8000/employee-set/'
const editPageURL = 'http://127.0.0.1:8000/edit_employee_info/'
const employeePk  = window.location.pathname.split('/')[2]


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

function employeeInfo() {	
	const apiURL = apiInfoURL + employeePk

	fetch(apiURL)
		.then(response => response.json())
		.then(data => {
			if (data.photo == null) {
				document.getElementById('photo').innerHTML = 'None'
			} else {
				document.getElementById('photo').innerHTML = `<img src="${data.photo}">`
			}
			document.getElementById('name').innerHTML     = data.name
			document.getElementById('position').innerHTML = data.position
			document.getElementById('salary').innerHTML   = data.salary
			if (data.parent == null) {
				document.getElementById('parent').innerHTML = 'None'
			} else {
				getParentName(data.parent, `${editPageURL}${data.parent}`)
			}
			document.getElementById('employment_date').innerHTML = data.employment_date
			})
}

function getParentName(id, url) {
	const apiParentNameURL = 'http://127.0.0.1:8000/chief-name/'+id
	fetch(apiParentNameURL)
		.then(response => response.json())
		.then(data => {
			document.getElementById('parent').innerHTML = `<a href="${url}">${data.name}</a>`			
		})
}

async function submitChanges() {
	let contextData = {
		name            : document.getElementById('name_input').value,
		position        : document.getElementById('position_input').value,
		salary          : document.getElementById('salary_input').value,
		parent          : document.getElementById('parent_input').value,
		employment_date : document.getElementById('employment_date_input').value,
	}

	const formData = new FormData()

	photo = document.querySelector('input[type="file"]').files[0]
	formData.append('photo', photo)
	for (let el in contextData) {
		if (contextData[el] != '') {
			formData.append(el, contextData[el])
		}
	}

	await fetch(`${apiInfoURL}${employeePk}`, {
		method : 'PATCH',
		headers : {
			'X-CSRFToken': getCookie('csrftoken'),
		},
		body: formData
	})
	employeeInfo()
}

employeeInfo()