const editPageURL = 'http://127.0.0.1:8000/edit_employee_info/'
const apiURL      = 'http://127.0.0.1:8000/employee-set/'

let name     = ''
let position = ''
let date     = ''
let salary   = ''

let orderBy = ''
let tableElements = []


function getRequestUrl() {
	const requestParams = `?name=${name}&position=${position}&date=${date}&salary=${salary}&order=${orderBy}`
	const requestURL = apiURL + requestParams

	return requestURL
}

async function addTableRows() {
	const url = getRequestUrl()
	tableElements = []

	await fetch(url)
		.then(response => response.json())
		.then(data => {
			data.map(el => {
				tableElements.push(el)
			})
		})
		pagination()
}

function pagination(index=1) {
	const itemsPerPage  = 10
	const numberOfPages = Math.ceil(tableElements.length / itemsPerPage)
	let   pageNumber    = index
	console.log(tableElements.length)
	console.log(itemsPerPage)
	console.log(numberOfPages)

	const firstItemIndex = (((pageNumber-1)*itemsPerPage))
	const lastItemIndex  = (pageNumber != numberOfPages) ? (firstItemIndex+10) : tableElements.length

	document.getElementsByTagName("tbody")[0].innerHTML = ''
	for (i=firstItemIndex; i<lastItemIndex; i++) {
		document.getElementsByTagName("tbody")[0].innerHTML +=
		`
		<tr class="tbody_tr">
			<td>${tableElements[i].name}</td>
			<td>${tableElements[i].position}</td>
			<td>${tableElements[i].employment_date}</td>
			<td>${tableElements[i].salary}</td>
			<td><img src="${tableElements[i].photo}"></td>
			<td><a href="${editPageURL+tableElements[i].id}">Edit</a></td>
			<td><a onclick="deleteEmployee(${tableElements[i].id})" href="#">Delete</a></td>
		</tr>
		`
	}

	document.getElementById("pagination").innerHTML = ''
	for (i=1; i<=numberOfPages; i++){
		document.getElementById("pagination").innerHTML +=
		`
		<button type='button' onclick="pagination(${i})">${i}</button>
		`
	}
}

function editSearchFields(index) {
	name     = document.querySelector('.thead_search').children[0].children[0].value
	position = document.querySelector('.thead_search').children[1].children[0].value
	date     = document.querySelector('.thead_search').children[2].children[0].value
	salary   = document.querySelector('.thead_search').children[3].children[0].value

	addTableRows()
}

function editOrderField(orderField) {
	if (orderBy === orderField) {
		orderBy = '-' + orderField
	} else {
		orderBy = orderField
	}

	addTableRows()
}


addTableRows(getRequestUrl())


document.querySelector('tr.thead_tr').querySelectorAll('th').forEach(headerCell => {
	headerCell.addEventListener('click', () => {
		const headerName = headerCell.innerHTML.toLowerCase().replace(' ', '_')
		
		editOrderField(headerName)
	})
})


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

async function deleteEmployee(id) {
	const url = apiURL + id

	await fetch(url, {
		method : 'DELETE',
		credentials: 'same-origin',
		headers : {
			'Content-Type' : 'application/json',
			'X-CSRFToken': getCookie('csrftoken')
		}
	})
}
