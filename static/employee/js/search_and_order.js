const apiURL = 'http://127.0.0.1:8000/employee-set/'

let name     = ''
let position = ''
let date     = ''
let salary   = ''

let orderBy = ''


function getRequestUrl() {
	const requestParams = `?name=${name}&position=${position}&date=${date}&salary=${salary}&order=${orderBy}`
	const requestURL = apiURL + requestParams

	return requestURL
}

function addTableRows() {
	const url = getRequestUrl()

	document.getElementsByTagName("tbody")[0].innerHTML = ''

	fetch(url)
		.then(response => response.json())
		.then(data => {
			data.map(el => {
				document.getElementsByTagName("tbody")[0].innerHTML += 
				`
					<tr class="tbody_tr">
						<td>${el.name}</td>
						<td>${el.position}</td>
						<td>${el.employment_date}</td>
						<td>${el.salary}</td>
						<td><a href="${apiURL+el.id}">Edit</a></td>
						<td><a href="#">Delete</a></td>
					</tr>
				`
			})
		})
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