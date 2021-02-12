// from data.js
var tableData = data;


// Identify the table and tbody
var tbody = d3.select('#ufo-tbody');

// test

//d3.json("/api/recipemetadata").then((recipes) => {
   //console.log(recipes)
//});

d3.json("/api/recipemetadata", function(recipes){
    console.log(recipes)
});

// Create function to generate and populate the table
function buildTable(tableData){

    // Dynamically build table
    tableData.forEach(record => {
        var row = tbody.append('tr');

////logic: if checked -- identify the status as checked and if not set status to unchecked; add a status true or flase to records pulled from API

            row.append('td').append('input').attr("type", "checkbox");    
            row.append('td').text(record['recipe_id']);
            row.append('td').text(record['recipe_title']);
            row.append('td').text(record['cooking_minutes']);
            row.append('td').text(record['health_score'])    
            row.append('td').text(record['source_url']);
            row.append('td').text(record['likes']);
            row.append('td').text(record['carbohydrates_serving']);
            row.append('td').text(record['servings']);
            row.append('td').text(record['calories_serving']);

        /* // Use Object.values as an alternate method
            Object.values(record).forEach(col => {
                row.append('td').text(col);        
            });
        */
    })
}

/// This would updated checked data (as checked/unchecked) to table when a second search is initiated, as well as, store in variable, 
///when clicking next page

function addcheckeddata(){
   
    var checkeddata = [];


}


function filterTable(){
    // Create a copy of tableData specifically for filtering
   
    var filteredData = tableData;

    console.log('filter table event')

    // capture value for all search fields */
    var query = d3.select('#query').property('value');
    var cuisine = d3.select('#cuisine').property('value');
    var type_of_recipe = d3.select('#type_of_recipe').property('value');
    var calories = d3.select('#calories').property('value');
    var cookingMinutes = d3.select('#cookingMinutes').property('value');

    var filterFields

    // Build an object of fields to run through 
    var filterFields = {
        'query': query,
        'cuisine': cuisine,
        'type_of_recipe': type_of_recipe, 
        'calories': calories,
        'cookingMinutes': cookingMinutes
    }



    // Remove empty keys from the list of filters to search
    Object.entries(filterFields).forEach(([key, val]) => {
        
        // Use !val to check for empty strings or nulls
        if(!val) { 
            delete filterFields[key];
        }
    });

    console.log('----filterFields----')
    console.log(filterFields)


    d3.json(`/api/recipemetadata?query=${query}&cuisine=${cuisine}`, function(data){
        console.log(data);
    });

    // d3.json(`/api/recipemetadata?query=${query}&cuisine=${cuisine}`).then(data => {
    //     console.log(data);
    // });


    
    
    

    // '/api/ingredients?query=pasta&cuisine=Italian&type_of_recipe=snack&calories<=400&cookingMinutes<=45'
    /*
    // Loop through each of the filter keys  
    Object.entries(filterFields).forEach(([key, value]) => {
        // Continue to refine the filteredData array 
        filterFieldsRequest.concat(`${key}=${value}&`)
    });

    str1.concat(' ', str2));
    
    filterFieldsRequest.join("")
    */

    filterFieldsRequest = ['pasta', 'Italian', '&', '&', '&']
    console.log(filterFieldsRequest)

    var returns_metadata = request.args.get(filterFieldsRequest)
    console.log('---returns_metadata---')
    console.log(returns_metadata)
    



    // Loop through each of the filter keys and return records from filteredData that match 
    Object.entries(filterFields).forEach(([key, value]) => {
        // Continue to refine the filteredData array 
        filteredData = filteredData.filter(row => row[key] == value);
    });

    console.log('----filteredData----')
    console.log(filteredData)

    // Clear out the tbody
    tbody.html('');

////  then add checked rows back in

    // Rebuild the filtered table using the buildTable function 
    buildTable(filteredData);    
}

// Clear out input fields in the Filter Form, wipe the Table, and rebuild the Table with pristine original data
function formReset() {
    document.getElementById("filter-form").reset(); 
    tbody.html('');
    buildTable(tableData);
};





// Identify web elements on the page
filterbtn = d3.select('#filter-btn');
resetbtn = d3.select('#reset-btn');
submitbtn = d3.select('#submit-btn');
queryfield = d3.select('#query')
cuisinefield = d3.select('#cuisine')
typeofrecipefield = d3.select('#type_of_recipe')
calories = d3.select('#calories')
cookingminutesfield = d3.select('#cookingMinutes')

// Add event listeners to the web elements
filterbtn.on('click', filterTable);
resetbtn.on('click', formReset);
submitbtn.on('click', addcheckeddata);
queryfield.on('change', filterTable);
cuisinefield.on('change', filterTable);
typeofrecipefield.on('change', filterTable);
calories.on('change', filterTable);
cookingminutesfield.on('change', filterTable);

// Call the function to initially load the table
buildTable(tableData);