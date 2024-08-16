/*
 * Determine if the provided value is "true":
 *
 * Many settings stored on the server are true/false,
 * but stored as string values, "true" / "false".
 *
 * This function provides a wrapper to ensure that the return type is boolean
 */
export function isTrue(value: any): boolean {
  if (value === true) {
    return true;
  }

  if (value === false) {
    return false;
  }

  let s = String(value).trim().toLowerCase();

  return ['true', 'yes', '1', 'on', 't', 'y'].includes(s);
}

/*
 * Resolve a nested item in an object.
 * Returns the resolved item, if it exists.
 *
 * e.g. resolveItem(data, "sub.key.accessor")
 *
 * Allows for retrieval of nested items in an object.
 */
export function resolveItem(obj: any, path: string): any {
  let properties = path.split('.');
  return properties.reduce((prev, curr) => prev?.[curr], obj);
}
