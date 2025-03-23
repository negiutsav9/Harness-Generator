import { NextResponse } from 'next/server';

// This is a mock implementation for development/testing
// In production, this would call the CBMC Verification module
export async function POST(request: Request) {
  try {
    const { source_code, harnesses } = await request.json();

    if (!source_code || !harnesses || !Array.isArray(harnesses)) {
      return NextResponse.json(
        { error: 'Source code and harnesses are required' },
        { status: 400 }
      );
    }

    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 3000));

    // Example mock response with verification results
    const results = harnesses.map((harness, index) => {
      // For demonstration, make the first harness fail and the second succeed
      const isSuccess = index % 2 === 1;

      return {
        function_name: harness.function_name,
        status: isSuccess ? 'success' : 'error',
        errors: isSuccess ? [] : [
          'Memory leak detected: Resource allocated on line 14 is not freed',
          'NULL pointer dereference possible on line 22'
        ],
        traces: isSuccess ? [] : [
          {
            line: 14,
            message: 'Memory allocated here'
          },
          {
            line: 28,
            message: 'Function returns without freeing memory'
          }
        ]
