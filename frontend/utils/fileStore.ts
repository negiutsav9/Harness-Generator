// File system related types and utilities

export interface FileNode {
  name: string;
  path: string;
  isDirectory: boolean;
  children?: FileNode[];
  content?: string;
}

/**
 * Updates the content of a file in the file structure tree
 */
export const updateFileContent = (
  files: FileNode[],
  path: string,
  newContent: string,
): FileNode[] => {
  return files.map((node) => {
    if (node.path === path && !node.isDirectory) {
      return { ...node, content: newContent };
    } else if (node.isDirectory && node.children) {
      return {
        ...node,
        children: updateFileContent(node.children, path, newContent),
      };
    }
    return node;
  });
};

/**
 * Finds a file node by path
 */
export const findFileByPath = (
  files: FileNode[],
  path: string,
): FileNode | null => {
  for (const file of files) {
    if (file.path === path) {
      return file;
    }

    if (file.isDirectory && file.children) {
      const found = findFileByPath(file.children, path);
      if (found) return found;
    }
  }

  return null;
};

/**
 * Converts a file tree to a flat list of files
 */
export const flattenFileTree = (files: FileNode[]): FileNode[] => {
  let result: FileNode[] = [];

  for (const file of files) {
    result.push(file);

    if (file.isDirectory && file.children) {
      result = [...result, ...flattenFileTree(file.children)];
    }
  }

  return result;
};

/**
 * Check if a file is a test file
 */
export const isTestFile = (file: FileNode): boolean => {
  // Check if the file path contains common test directory names
  const testDirPattern = /[\\/](test|tests|spec|specs|__tests__)[\\/]/i;
  if (testDirPattern.test(file.path)) {
    return true;
  }

  // Check if the filename follows test naming patterns
  const testFilePattern = /\.(test|spec)\.(c|cpp|h|hpp)$/i;
  if (testFilePattern.test(file.name)) {
    return true;
  }

  // Check if the filename starts with "test_" or "spec_"
  if (/^(test_|spec_)/.test(file.name)) {
    return true;
  }

  return false;
};

/**
 * Gets all C/C++ source files from a file tree (excluding test files)
 */
export const getSourceFiles = (files: FileNode[]): FileNode[] => {
  return flattenFileTree(files).filter(
    (file) =>
      !file.isDirectory && /\.(c|cpp)$/i.test(file.name) && !isTestFile(file),
  );
};

/**
 * Gets all header files from a file tree (excluding test files)
 */
export const getHeaderFiles = (files: FileNode[]): FileNode[] => {
  return flattenFileTree(files).filter(
    (file) =>
      !file.isDirectory && /\.(h|hpp)$/i.test(file.name) && !isTestFile(file),
  );
};

/**
 * Builds a combined source file from all files in the tree, excluding test files
 */
export const combineSourceFiles = (files: FileNode[]): string => {
  // Get both source and header files, excluding test files
  const headerFiles = getHeaderFiles(files);
  const sourceFiles = getSourceFiles(files);

  console.log(
    `Combining ${headerFiles.length} header files and ${sourceFiles.length} source files, excluding test files`,
  );

  // First include headers
  let combined = headerFiles
    .map((file) => `// Header File: ${file.path}\n${file.content || ""}\n\n`)
    .join("");

  // Then include source files
  combined += sourceFiles
    .map((file) => `// Source File: ${file.path}\n${file.content || ""}\n\n`)
    .join("");

  return combined;
};
