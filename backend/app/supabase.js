require('dotenv').config();

const SUPABASE_URL = process.env.supaurl;
const SUPABASE_ANON_KEY = process.env.supakey;

const data = {
  information: "he"
};

async function uploadData() {
  try {
    const response = await fetch(`${SUPABASE_URL}/rest/v1/Papers`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
      },
      body: JSON.stringify(data),
    });

    console.log('Response Status:', response.status);

    if (response.status === 204) {
      console.log('No content returned from Supabase');
    } else {
      const result = await response.json();
      console.log('Response Body:', result);
      if (response.ok) {
        console.log('Data uploaded successfully:', result);
      } else {
        console.error('Error uploading data:', result);
      }
    }
  } catch (error) {
    console.error('An error occurred:', error);
  }
}

uploadData();