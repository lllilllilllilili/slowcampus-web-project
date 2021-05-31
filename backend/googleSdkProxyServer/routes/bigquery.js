var express = require('express');
var router = express.Router();
const {BigQuery} = require('@google-cloud/bigquery');

const feature=async(res, category)=>{
  const bigquery = new BigQuery();
  
  const query = "SELECT * FROM `fluid-crane-284202.prototyping_dataset.feature_basic` WHERE category="+"'"+category+"'";
  const options = {
    query : query,
    location: 'US',
  } 
  const [job] = await bigquery.createQueryJob(options);
  const [rows] = await job.getQueryResults();
  rows.forEach(row=>console.log(row));
  res.send([rows])
}



const query=async(res, category)=>{
  // Queries the U.S. given names dataset for the state of Texas.
  const bigquery = new BigQuery();
 
  const query = "SELECT * FROM `fluid-crane-284202.prototyping_dataset.category_basic` WHERE category="+"'"+category+"'";
  console.log(query)
  console.log(category)
  //const query = "SELECT name FROM \`bigquery-public-data.usa_names.usa_1910_2013\` WHERE state = 'TX' LIMIT 100";
  // For all options, see https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query
  const options = {
    query: query,
    // Location must match that of the dataset(s) referenced in the query.
    location: 'US',
  };

  // Run the query as a job
  const [job] = await bigquery.createQueryJob(options);
  console.log(`Job ${job.id} started.`);

  // Wait for the query to finish
  const [rows] = await job.getQueryResults();
  
  // Print the results
  console.log('Rows:');
  rows.forEach(row => console.log(row));
  
  res.send([rows])

}

const category_advanced=async(res, category)=>{
  const bigquery = new BigQuery();
  
  const query = "SELECT * FROM `fluid-crane-284202.prototyping_dataset.category_advanced` WHERE category="+"'"+category+"'";
  const options = {
    query : query,
    location: 'US',
  } 
  const [job] = await bigquery.createQueryJob(options);
  const [rows] = await job.getQueryResults();
  rows.forEach(row=>console.log(row));
  res.send([rows])
}

const commit=async(res, category)=>{
  const bigquery = new BigQuery();
  const query = "SELECT * FROM `fluid-crane-284202.prototyping_dataset.commit_basic` WHERE category="+"'"+category+"'";
  const options = {
    query : query,
    location: 'US',
  }
  const [job] = await bigquery.createQueryJob(options);
  const [rows] = await job.getQueryResults();
  rows.forEach(row=>console.log(row));
  res.send([rows])
}

const streaming=async(res, category)=>{
  const bigquery = new BigQuery();
  const query = "SELECT payloadString FROM `fluid-crane-284202.prototyping_dataset.category_streaming_data_error_records` WHERE payloadString like"+"'%"+category+"%'";
  const options = {
    query : query,
    location: 'US',
  }
  const [job] = await bigquery.createQueryJob(options);
  const [rows] = await job.getQueryResults();
  rows.forEach(row=>console.log(row));
  if(rows.length == 0)
    res.send(['nodata'])
  else
    res.send([rows])
}

/* POST users listing. */
router.post('/', async function(req, res, next) {
  //res.json(users);
  res.set({'access-control-allow-origin':'*'});
  await query(res, req.query.category)
});

/* POST users listing. */
router.post('/feature', async function(req, res, next) {
  //res.json(users);
  res.set({'access-control-allow-origin':'*'});
  await feature(res, req.query.category)
});

/* POST users listing. */
router.post('/category_advanced', async function(req, res, next){
  res.set({'access-control-allow-origin':'*'});
  await category_advanced(res, req.query.category)
});


router.post('/commit', async function(req, res, next){
  res.set({'access-control-allow-origin':'*'});
  await commit(res, req.query.category);
});

router.post('/streaming', async function(req, res, next){
  res.set({'access-control-allow-origin':'*'});
  await streaming(res, req.query.category);
});

module.exports = router;
