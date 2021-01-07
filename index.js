const { createPow, powTypes } = require("@textile/powergate-client");
const host = "http://localhost:6002"; // or whatever powergate instance you want
const fs = require("fs")
const pow = createPow({ host });
const token = "c01b37d8-2030-49ce-a47f-95170b2a3331";
pow.setToken(token);
/getFile/{cid}
async function exampleCode() {
  // const { user } = await pow.admin.users.create() // save this token for later use!
  // // pow.setToken
  // await console.log(JSON.stringify(user))

  // // get wallet addresses associated with the user
  // const { addressesList } = await pow.wallet.addresses();
  // console.log(addressesList);

  // const buffer = fs.readFileSync(`package.json`);
  // const { cid } = await pow.data.stage(buffer);

  // // store the data using the default storage configuration
  // const { jobId } = await pow.storageConfig.apply(cid,{override:true});

  // // watch the job status to see the storage process progressing
  // const jobsCancel = pow.storageJobs.watch((job) => {
  //     console.log("job canceled");
  //   if (job.status === powTypes.JobStatus.JOB_STATUS_CANCELED) {
  //   } else if (job.status === powTypes.JobStatus.JOB_STATUS_FAILED) {
  //     console.log("job failed");
  //   } else if (job.status === powTypes.JobStatus.JOB_STATUS_SUCCESS) {
  //     console.log("job success!");
  //   }
  // }, jobId);

  // // watch all log events for a cid
  // const logsCancel = pow.data.watchLogs((logEvent) => {
  //   console.log(`received event for cid ${logEvent.cid}`);
  // }, cid);
  cid = 'QmXABPHbuBkVfz8y1q9UyWtwkVVFRhi8k7LMUGmJMideys';
  // const { cidInfosList } = await pow.data.cidInfo(cid)
  console.log(cid);
  // retrieve data stored in the user by cid
  const bytes = await pow.data.get(cid)
  console.log('File is \n'+new Buffer.from(bytes).toString())
}

exampleCode();

//{"id":"d9f57b18-dea8-4a1f-9c6a-6a5c5f78d157","token":"eff54759-d0b7-4ad1-8d0f-6d86446d37b1"}
