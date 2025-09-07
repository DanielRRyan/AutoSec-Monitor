<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">🚨 CVE Alert Dashboard</h1>

    <button
      @click="fetchCVEAlerts"
      class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
    >
      🔄 Run CVE Scan
    </button>

    <div v-if="loading" class="mt-4">Loading CVEs...</div>
    <div v-else class="mt-6 space-y-4">
      <div
        v-for="alert in cveAlerts"
        :key="alert.package"
        class="bg-white shadow-md p-4 rounded"
      >
        <h2 class="text-lg font-semibold text-blue-800">{{ alert.package.toUpperCase() }}</h2>
        <ul class="list-disc pl-5 mt-2">
          <li v-for="entry in alert.entries" :key="entry.id" class="mb-2">
            <span class="font-bold">{{ entry.id }}</span> – {{ entry.description.slice(0, 100) }}...
            <div class="text-sm text-gray-500">Published: {{ formatDate(entry.published) }}</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useQuery, useMutation, gql } from '@apollo/client/core'

const CVE_SCAN_MUTATION = gql`
  mutation {
    scanCves {
      package
      entries {
        id
        description
        published
        source
      }
    }
  }
`

const cveAlerts = ref([])
const loading = ref(false)

const fetchCVEAlerts = async () => {
  loading.value = true
  try {
    const { data } = await apolloClient.mutate({
      mutation: CVE_SCAN_MUTATION
    })
    cveAlerts.value = data.scanCves
  } catch (error) {
    console.error("GraphQL error:", error)
  } finally {
    loading.value = false
  }
}

const formatDate = (isoString) => {
  return new Date(isoString).toLocaleDateString()
}
</script>

<style scoped>
body {
  background-color: #f7f9fc;
}
</style>
